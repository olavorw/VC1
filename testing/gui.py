import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Windows.Forms import Application, Form, Label, TextBox, Button, CheckBox, RadioButton # type: ignore
from System.Drawing import Point, Size, Icon # type: ignore

class SimpleForm(Form):
    def __init__(self):
        super(SimpleForm, self).__init__()
        self.Text = 'VC1 {version} {status}'
        self.Size = Size(300, 200)
        
        # Set custom icon
#        self.Icon = Icon("assets/logo/VC1.ico")

        # Random Label
        label = Label()
        label.Text = 'Random Label'
        label.Location = Point(10, 10)
        self.Controls.Add(label)

        # Random TextBox
        textbox = TextBox()
        textbox.Location = Point(10, 40)
        self.Controls.Add(textbox)
        
        # Random Button
        button = Button()
        button.Text = 'Random Button'
        button.Location = Point(10, 70)
        button.Click += self.button_click
        self.Controls.Add(button)
        
        # Random CheckBox
        checkbox = CheckBox()
        checkbox.Text = 'Random CheckBox'
        checkbox.Location = Point(10, 100)
        self.Controls.Add(checkbox)
        
        # Random RadioButton
        radiobutton = RadioButton()
        radiobutton.Text = 'Random RadioButton'
        radiobutton.Location = Point(10, 130)
        self.Controls.Add(radiobutton)

    def button_click(self, sender, event):
        print("Button clicked")

Application.EnableVisualStyles()
form = SimpleForm()
Application.Run(form)
