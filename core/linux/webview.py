import gi
import sys
import threading

gi.require_version("Gtk", "3.0")
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, Gdk, WebKit2

from json import dumps

class MacronWebview:
  def __init__(self, window, config):
    self.webview = WebKit2.WebView()

    if "devServerURI" in config:
      self.load(config["devServerURI"])
    elif "sourcePath" in config:
      sourcePath = 'file://' + (config["rootPath"] + config["sourcePath"]).replace("//", "\u005c")

      self.load(
        sourcePath
      )

    # Load main macron JavaScript APIs
    self.evaluate_script(r'var macron = {};')
    
    with open('../../src/init.js') as f:
      self.evaluate_script(f.read())

    with open('../../src/polyfills/require.js') as f:
      self.evaluate_script(f.read())

    # with open('../../src/front/window.js') as f:
    #   self.evaluate_script(f.read())

    # Create macron.CurrentWindow
    self.evaluate_script('macron.CurrentWindow = {};'.format(dumps(config)))

    # TODO: Add inspector. JS APIs need logging.
    # inspector = self.webview.get_inspector()
    # inspector.connect('inspect-web-view', get_webkit_inspector)
    # inspector.attach()
    # inspector.show()

  def evaluate_script(self, script):
    self.webview.run_javascript(script)

  def triggerEvent(self, event):
    self.evaluate_script(
      '''macron.CurrentWindow.eventCallbacks.{}.forEach(
        function(callback) {{
          eval(
            "(" + callback.replace(/\\/\\//gi, '\\\\').replace(/\/.?/gi, '').replace(/\\'\\'\\'/gi, "\\"") + ")();"
          )
        }}
      );
      '''.format(event)
    )

  # Gets the Uri of the current document hosted in the WebBrowser.
  def getSource(self):
    return self.webview.get_uri()

  # Sets the Uri of the current document hosted in the WebBrowser.
  # @param uri {string}
  # TODO change setSource to load (in Windows port)
  def load(self, uri):
    self.webview.load_uri(uri)

  # Reloads the current page with optional cache validation.
  # If noCache is true, the WebBrowser control refreshes
  # without cache validation by sending a "Pragma:no-cache"
  # header to the server.
  # @param noCache {bool}
  # TODO test
  def refresh(self, noCache=False):
    if noCache:
      self.webiew.reload()
    else:
      self.webiew.reload_bypass_cache()

  # Navigate back to the previous document, if there is one.
  # TODO test
  def goBack(self):
    self.webview.go_back()

  # Navigate forward to the next document, if there is one.
  # TODO test
  def goForward(self):
    self.webview.go_forward()
