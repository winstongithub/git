
from ctypes import c_void_p

from OpenGL import GL

from glwrap import glGenVertexArray
from OpenGL.GLUT import *

null = c_void_p(0)

# This is lame. What's the right way to get the sizeof(GLfloat) ?
# Tried sys.getsizeof(GLfloat), sys.getsizeof(GLfloat()),
# GLfloat().__sizeof__(). All give different wrong answers (size of python
# objects, not of underlying C 'float' type)
sizeOfFloat = 4

# Three vertices, with an x,y,z & w for each.
vertexPositions =  [ -1.0, -1.0, 0.0, 1.0, -1.0, 0.0, 0.0,1.0, 0.0 ]
vertexComponents = 3

# So that the shaders work on my OpenGL2.1 hardware, I've removed the
# 'version 330' line, and have stopped requesting a layout location for the
# vertex position.
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
   outputColor = vec4(1.0f, 1.0f, 1.0f, 1.0f);
}
"""


window = None

# Integer handle identifying our compiled shader program
theProgram = None

# Integer handle identifying the GPU memory storing our vertex position array
positionBufferObject = None




def initialize_vertex_buffer():
    global positionBufferObject
    positionBufferObject = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, positionBufferObject)
    array_type = (GL.GLfloat * len(vertexPositions))
    GL.glBufferData(
        GL.GL_ARRAY_BUFFER, len(vertexPositions) * sizeOfFloat,
        array_type(*vertexPositions), GL.GL_STATIC_DRAW
    )
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)


# Called once at application start-up.
# Must be called after we have an OpenGL context, i.e. after the pyglet
# window is created
def init():
    initialize_vertex_buffer()


# Called to redraw the contents of the window
def display():
    GL.glClearColor(0.0, 0.0, 0.0, 0.0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

 #   GL.glUseProgram(theProgram)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, positionBufferObject)
    GL.glEnableVertexAttribArray(0)
    GL.glVertexAttribPointer(0, vertexComponents, GL.GL_FLOAT, False, 0, null)

    GL.glDrawArrays(GL.GL_TRIANGLES, 0, len(vertexPositions) // vertexComponents)

    GL.glDisableVertexAttribArray(0)
  #  GL.glUseProgram(0)

    # equivalent of glutSwapBuffers and glutPostRedisplay is done for us by
    # pyglet


# Called when the window is resized, including once at application start-up
#def reshape(width, height):
 #   GL.glViewport(0, 0, width, height)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow("test".encode())
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop() 


if __name__ == '__main__':
    main()

