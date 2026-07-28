async function sendMessage() {

    let input = document.getElementById("user-input");
    let chat = document.getElementById("chat-box");

    let message = input.value;

    if(message=="")
        return;

    chat.innerHTML +=
        "<p><b>You:</b> " + message + "</p>";

    input.value="";

    const response = await fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    });

    const data = await response.json();

    chat.innerHTML +=
        "<p><b>Bot:</b> " + data.reply + "</p>";

    chat.scrollTop = chat.scrollHeight;
}