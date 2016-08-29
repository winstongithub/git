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

def rotate( x=None , y=None , z=None ):
    mat4=np.eye(4)
    if x != None:
        mat4= np.dot(np.array([[ 1,0,0,0],[0,np.cos(x),-np.sin(x),0]
                      ,[0,np.sin(x),np.cos(x),0],[0,0,0,1]],float),mat4)
    if y != None:
        mat4= np.dot(np.array([[ np.cos(y),0,np.sin(y),0],[0,1,0,0]
                      ,[-np.sin(y),0,np.cos(y),0],[0,0,0,1]],float),mat4)

    if z != None:
        mat4= np.dot(np.array([[ np.cos(z),-np.sin(x),0,0],[np.sin(z),np.cos(x),0,0]
                      ,[0,0,1,0],[0,0,0,1]],float),mat4)
    return mat4
                     
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
    transMat = np.dot(rotate(np.pi,np.pi,np.pi) , transMat)
    transMat = np.dot( scale( 0.4 ,0.4 ,0.4 ) , transMat)
    newList=[]
    for i in range( 0 , len(array)):
        perArray = np.dot( transMat , array[i])
        newList.append( perArray.tolist())
    return np.array(newList,float )
    
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
