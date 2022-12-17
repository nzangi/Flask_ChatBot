class Chatbox{
    constructor(){
    this.args = {
        openButton: document.querySelector('.chatbox_button'),
        chatBox: document.querySelector('.chatbox_support'),
        sendButton: document.querySelector('.send_button')
    }
    this.state = false;
    this.messages = [];
    }
    display(){
        const {openButton,chatBox,sendButton} = this.args;
        openButton.addEventListener('click',() => this.toggleState(chatBox))

        sendButton.addEventListener('click',() => this.onSendButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup",({key}) => {
            if(key === "Enter"){
                this.onSendButton(chatBox)
            }
        })

    }
    toggleState(chatBox){
    this.state = !this.state;
    if(this.state){
        chatBox.classList.add('chatbox--active')
    }else{
        chatBox.classList.remove("chatbox--active")
        }
    }

    onSendButton(chatBox){
        var textField = chatBox.querySelector('input');
        let text1 = textField.value
        if (text1 === ""){
            return;
        }

        let msg1 = {name : "User", message : text1}
        this.messages.push(msg1);

        fetch('http://127.0.0.1:5000/predict',{
            method: 'POST',
            body: JSON.stringify({message: text1}),
            mode: 'cors',
            headers:{
                'Content-Type':'application/json'
            },
            })
            .then(r => r.json())
            .then(r => {
                 let msg2 = {name: "Nzangi" ,message: r.answer};
                 console.log(msg2);
                 this.messages.push(msg2);
                 this.updateChatText(chatBox)
                 textField.value = ''
            }).catch((error) => {
                console.error('Error:',error);
                this.updateChatText(chatBox)
                textField.value = ''
            });
    }
    updateChatText(chatBox){
        var html = '';
        this.messages.slice().reverse().forEach(function(item,){
            if(item.name === "Nzangi"){
                    html += '<div class= "messages_item messages_item--visitor">' + item.message + '</div>'
            }
            else{
                    html += '<div class= "messages_item messages_item--operator">' + item.message + '</div>'

            }
        });
        const chatmessage = chatBox.querySelector('.chatbox_messages');
        chatmessage.innerHTML = html;
        }
    }
const chatbox = new Chatbox();
chatbox.display();