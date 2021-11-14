package com.netChat.java;

import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.UIManager;
import javax.swing.border.EmptyBorder;
import javax.swing.text.DefaultCaret;

public class ClientWindow extends JFrame implements Runnable {
	
	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JTextField txtMessage;
	private JTextArea history;
	private DefaultCaret caret;
	private DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
	private Thread run, listen;
	private Client client;
	private boolean running = false;
	
	// client window method
	public ClientWindow(String name, String address, int port) {
		setTitle("Chat Client");
		client = new Client(name, address, port);
		// try connection, if failed say so
		boolean connect = client.openConnection(address);
		if (!connect) {
			System.err.println("Connection failed!");
			console("Connection failed!");
		}
		createWindow();
		console("Attempting a connection to " + address + ":" + port +", user: " + name);
		String connection = "/c/" + name;
		client.send(connection.getBytes());
		run = new Thread(this, "Running");
		running = true;
		run.start();
	}
		
	// window method
	private void createWindow() {
		try {
			UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
		} catch (Exception e) {
			e.printStackTrace();
		}
			
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(880, 550);
		setLocationRelativeTo(null);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		GridBagLayout gbl_contentPane = new GridBagLayout();
		gbl_contentPane.columnWidths = new int[]{28, 815, 30, 7};
		gbl_contentPane.rowHeights = new int[]{35, 475, 40};
		gbl_contentPane.columnWeights = new double[]{1.0, 1.0};
		gbl_contentPane.rowWeights = new double[]{1.0, Double.MIN_VALUE};
		contentPane.setLayout(gbl_contentPane);
			
		// where the messages are displayed
		history = new JTextArea();
		history.setEditable(false);
		JScrollPane scroll = new JScrollPane(history);
		GridBagConstraints scrollConstraints = new GridBagConstraints();
		scrollConstraints.insets = new Insets(0, 0, 5, 5);
		scrollConstraints.fill = GridBagConstraints.BOTH;
		scrollConstraints.gridx = 0;
		scrollConstraints.gridy = 0;
		scrollConstraints.gridwidth = 3;
		scrollConstraints.gridheight = 2;
		scrollConstraints.insets = new Insets(0, 5, 0, 0);
		contentPane.add(scroll, scrollConstraints);
			
		// text box to write out message
		txtMessage = new JTextField();
		// send message with enter key
		txtMessage.addKeyListener(new KeyAdapter() {
			public void keyPressed(KeyEvent e) {
				if (e.getKeyCode() == KeyEvent.VK_ENTER) {
					send(txtMessage.getText(), true);
				}
			}
		});
		GridBagConstraints gbc_txtMessage = new GridBagConstraints();
		gbc_txtMessage.insets = new Insets(0, 0, 0, 5);
		gbc_txtMessage.fill = GridBagConstraints.HORIZONTAL;
		gbc_txtMessage.gridx = 0;
		gbc_txtMessage.gridy = 2;
		gbc_txtMessage.gridwidth = 2;
		contentPane.add(txtMessage, gbc_txtMessage);
		txtMessage.setColumns(10);
			
		// button to call send method with message
		JButton btnSend = new JButton("Send");
		btnSend.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				send(txtMessage.getText(), true);
			}
		});
		// the grid everything is tied to 
		GridBagConstraints gbc_btnSend = new GridBagConstraints();
		gbc_btnSend.insets = new Insets(0, 0, 0, 5);
		gbc_btnSend.gridx = 2;
		gbc_btnSend.gridy = 2;
		contentPane.add(btnSend, gbc_btnSend);
		
		addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent e) {
				running = false;
				String disconnect = "/d/" + client.getID() + "/e/";
				send(disconnect, false);
				client.close();
			}
		});
			
		setVisible(true);
			
		txtMessage.requestFocusInWindow();
	}
	
	// set to listening for connections
	public void run() {
		listen();
	}
	
	// send messages to console
		private void send(String message, boolean text) {
			// if blank don't sent
			if (message.equals("")) return;
			if (text) {
			LocalDateTime now = LocalDateTime.now();
			message = client.getName() + ": " + message + " " + now.format(dtf);
			message = "/m/" + message;
			}
			client.send(message.getBytes());
			txtMessage.setText("");
		}
		
		// listen for connections
		public void listen() {
			listen = new Thread("Listen") {
				public void run() {
					while (running == true) {
						String message = client.receive();
						if (message.startsWith("/c/")) {
							client.setID(Integer.parseInt(message.split("/c/|/e/")[1]));
							console("Successfully connected to server! ID: " + client.getID());
						} else if (message.startsWith("/m/")) {
							String text = message.substring(3);
							text = text.split("/e/")[0];
							console(text);
						} else if (message.startsWith("/i/")) {
							String text = "/i/" + client.getID() + "/e/";
							send(text, false);
						} else if (message.startsWith("/u/")) {
							//String[] u = message.split("/u/|/n/|/e/");
							//users.update(Arrays.copyOfRange(u, 1, u.length - 1));
						}
					}
				}
			};
			listen.start();
		}
		
		// method for the console, where all the messages show up
		public void console(String message) {
			history.append(message + "\n\r");
			history.setCaretPosition(history.getDocument().getLength());
		}

		
}
