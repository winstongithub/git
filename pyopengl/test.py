from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def transToArray( lists , n ):
    size = len(lists)
    array = []
    for i in range( 0 , size//n ):
        l=lists[ i*n: i*n + n ]
        l.append(1)
        array.append( l )
    return np.array( array , float )

def transle( x=0 , y=0 , z=0 ):
    mat4=np.eye(4)
    mat4[0][3]=x
    mat4[1][3]=y
    mat4[2][3]=z
    return mat4

def rotate( angle , x=0 , y=0 , z=0 ):
    mat4=np.eye(4)
    if (x+y+z)==0:
        return mat4
    else:
        c= np.cos(angle)
        s=np.sin(angle)
        rotaMat4 = np.array([[ x**2*(1-c)+c , x*y*(1-c)-z*s , x*z*(1-c)+y*s , 0],
                             [x*y*(1-c)+z*s , y**2*(1-c)+c , y*z*(1-c)-x*s , 0],
                             [x*z*(1-c)-y*s , y*z*(1-c)+x*s , z**2*(1-c)+c , 0 ],
                             [0 , 0 , 0 ,1]
                             ],float)
        
    return rotaMat4
                     
def scale( x=1 , y=1 ,z=1 ):
    mat4=np.eye(4)
    mat4[0][0] = x
    mat4[1][1] = y
    mat4[2][2] = z
    return mat4
    
vertexbuffer = 0;

def runModelTrans( g):
    array = transToArray( g , 3 )
    transMat = transle(x=0.4 , y=0.4,z=0.4)
    transMat = np.dot(rotate(np.pi,0,0,1) , transMat)
    transMat = np.dot( scale( 0.4 ,0.4 ,0.4 ) , transMat)
    transMat = np.dot( setLookAtMat( 0 , 0 , 0 , 0,0,1, 0 ,1,0) ,transMat )
    transMat = np.dot( preProjectionMatrix( np.pi/4 , 1 , 1, 1000),transMat)
    newList=[]

    for i in range( 0 , len(array)):
        perArray = np.dot( transMat , array[i])
        newList.append( perArray.tolist())
    return np.array(newList,float )

def norMalize( v ):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    else:
        return v/norm

def setLookAtMat( eyex ,eyey , eyez , centerx , centery ,centerz , upx , upy , upz):
    p = np.array([ eyex , eyey ,eyez , 1 ],float )
    l = np.array([ centerx , centery , centerz , 1 ],float)
    u = np.array([upx,upy,upz,0],float)
    d = l-p
    r = np.cross( u[0:3] , d[0:3] )
    u=norMalize(u)
    d=norMalize(d)
    r=norMalize(r)
    r=r.tolist()
    r.append(0)
    r = np.array(r,float)

    x = -np.dot( p , r )
    y = -np.dot( p , u )
    z = -np.dot(p ,d )

    r[3] = x
    u[3] = y
    d[3] = z
    mat4= np.array([ r , u , d ,[ 0 , 0 , 0 , 1 ] ], float)
    return mat4

def preProjectionMatrix( fov , aspect , zn ,zf ):
    mat4 = np.eye(4)
    mat4[0][0] = 1/( np.tan( fov * 0.5) * aspect)
    mat4[1][1] = 1/ np.tan( fov * 0.5 )
    mat4[2][2] = zf / (zf - zn)
    mat4[3][2] = 1.0
    mat4[2][3] = (zn * zf )/(zn-zf)
    return mat4
def init():
    global vertexbuffer
    vertexbuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
    g_vertex_buffer_data = [ -1.0, -1.0, 0.0, 1.0, -1.0, 0.0, 0.0,1.0, 0.0 ]
    a = runModelTrans( g_vertex_buffer_data )
    vertex_list = a.flatten().tolist()
    ddata_buffer = (GLfloat*len(vertex_list))(*vertex_list)
    glBufferData(GL_ARRAY_BUFFER,len(vertex_list) * 4,ddata_buffer, GL_STATIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
 
def Draw():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(
		0,                  #attribute 0. No particular reason for 0, but must match the layout in the shader.
		4,                  # size
		GL_FLOAT,           # type
		False,           # normalized?
		0,                  # stride
		None           # array buffer offset
		)
    glDrawArrays(GL_TRIANGLES, 0, 3);
    glDisableVertexAttribArray(0);
    glFlush()

if __name__=="__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow("test".encode())
    init()
    glutDisplayFunc(Draw)
    glutIdleFunc(Draw)
    glutMainLoop() 
