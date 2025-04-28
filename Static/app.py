from flask import Flask, render_template, request
import serial
import serial.tools.list_ports
import time
import atexit

# Create Flask app
app - Flask(__name__)
