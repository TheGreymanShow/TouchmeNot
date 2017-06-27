import kivy
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.button import Button

class HelloCount(App):
	count=NumericProperty(0)
	
	def build(self):
		self.bind(count=self.update_widg)
		self.btn=Button(name = "Hello",font_size="20dp")
		self.btn.bind(on_press=self.increment)
		return self.btn

	def increment(self,button):
		self.count +=1
		
	def update_widg(self,app,value):
		self.btn.text="hello {}".format(self.count)		

if __name__ == "__main__":
	HelloCount().run()	