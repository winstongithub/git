from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL.shaders import compileShader, compileProgram
strVertexShader = """
#version 120

in vec4 position;
void main()
{
   gl_Position = position;
}
"""
strFragmentShader = """
#version 120

out vec4 outputColor;
void main()
{
   outputColor = vec4(1.0f, 0.0f, 0.0f, 1.0f);
}
"""

vertexbuffer = 0;
shader = None
def init():
    global shader
    shader = compileProgram(
            compileShader( strVertexShader , GL_VERTEX_SHADER ) ,
            compileShader( strFragmentShader , GL_FRAGMENT_SHADER)
        )
    global vertexbuffer
    vertexbuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
    g_vertex_buffer_data = [ -1.0, -1.0, 0.0, 1.0, -1.0, 0.0, 0.0,1.0, 0.0 ]
    ddata_buffer = (GLfloat*len(g_vertex_buffer_data))(*g_vertex_buffer_data)
    glBufferData(GL_ARRAY_BUFFER,len(g_vertex_buffer_data) * 4,ddata_buffer, GL_STATIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
 
def Draw():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(shader)
    glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(
		0,                  #attribute 0. No particular reason for 0, but must match the layout in the shader.
		3,                  # size
		GL_FLOAT,           # type
		False,           # normalized?
		0,                  # stride
		None           # array buffer offset
		)
    glDrawArrays(GL_TRIANGLES, 0, 3);
    glDisableVertexAttribArray(0);
    glUseProgram(0)
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
