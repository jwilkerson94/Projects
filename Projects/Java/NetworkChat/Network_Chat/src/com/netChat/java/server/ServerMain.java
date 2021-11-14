package com.netChat.java.server;

public class ServerMain {
	
	private int port;
	private Server server;
	
	public ServerMain(int port) {
		this.port = port;
		server = new Server(port);
	}
	
	
	public static void main(String[] args) {
		int port;
		// check if a port was specified
		if (args.length != 1) {
			System.out.println("Usage: java -jar netChatServer.jar [port] ");
			return;
		}
		port = Integer.parseInt(args[0]);
		new ServerMain(port);
	}
}
