package Jade;

import static org.lwjgl.glfw.GLFW.GLFW_PRESS;
import static org.lwjgl.glfw.GLFW.GLFW_RELEASE;

public class KeyListener {
    // variables
    private static KeyListener instance;
    private boolean keyPressed[] = new boolean[350];

    // constructor
    private KeyListener() {

    }

    // get instance of keylistener
    public static KeyListener get() {
        if (KeyListener.instance == null) {
            KeyListener.instance = new KeyListener();
        }

        return KeyListener.instance;
    }

    // set action if the key is pressed
    public static void keyCallback(long window, int key, int scancode, int action, int mods) {
        if (action == GLFW_PRESS) {
            get().keyPressed[key] = true;
        } else if (action == GLFW_RELEASE) {
            get().keyPressed[key] = false;
        }
    }

    // get keypressed
    public static boolean isKeyPressed(int keyCode) {
            return get().keyPressed[keyCode];
        }
}

