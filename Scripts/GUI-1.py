from guizero import App, Text, TextBox, PushButton, Slider, Picture

def say_name():
    welcome_msg.value = my_name.value

def change_title_size(slider_value):
    welcome_msg.size = slider_value


app = App(title="Test GUI")

welcome_msg = Text(app, text="\nWelcome to this test GUI", size=16)
my_name = TextBox(app, width=50)
update_title = PushButton(app, command=say_name, text="Display my name")
text_size = Slider(app, command=change_title_size, start=10, end=40)
my_test_image = Picture(app, image="test.gif")

app.display()
