let round_places = []
let round = 0;
let last_char_p2;
let round_repeated = false;
const roomName = JSON.parse(document.getElementById('room_name').textContent);
const userName = JSON.parse(document.getElementById('username').textContent);

const socket = new WebSocket(`wss://${window.location.host}/ws/${roomName}/`);

socket.addEventListener('open', (event) => {
        const chat_th = document.querySelector('#chat-th')
        const col = document.createElement('th');
        col.appendChild(document.createTextNode(userName))
        chat_th.appendChild(col)
        col.classList.add("px-4");
        col.classList.add("py-2");
        col.classList.add(userName);
})

socket.onmessage = event => {
    const data = JSON.parse(event.data);
    if (data.message) {
        const class_name = `.${data.username}`;
        if (data.username != userName && ! document.querySelector(class_name)) {
            const chat_th = document.querySelector('#chat-th')
            const col = document.createElement('th');
            col.appendChild(document.createTextNode(data.username))
            col.classList.add("px-4");
            col.classList.add("py-2");
            col.classList.add(data.username);
            chat_th.appendChild(col)
        }
        const table = document.querySelector('#chat-tbody');
        last_char_p2 = data.message[data.message.length-1];
        //const table = document.querySelector(`.${data.username}`);
        const tdata = document.createElement("td");
        tdata.classList.add("border");
        tdata.classList.add("px-4");
        tdata.classList.add("py-2");
        tdata.classList.add("bg-white");
        tdata.appendChild(document.createTextNode(data.message));
        if (data.username == userName) {
            const row = document.createElement('tr');
            row.appendChild(tdata)
            table.appendChild(row)
        } else {
            let row;
            if (table.lastChild.data == "\n  "){
                row = document.createElement('tr');
                const p2_tdata = document.createElement("td");
                p2_tdata.classList.add("border");
                p2_tdata.classList.add("px-4");
                p2_tdata.classList.add("py-2");
                p2_tdata.classList.add("bg-white");
                p2_tdata.appendChild(document.createTextNode(''));
                row.appendChild(p2_tdata);
            }else {
                row = table.lastElementChild;
            }
            row.appendChild(tdata);
            table.appendChild(row);
        }
        let url = `http://${window.location.host}/world-atlas/api/places/exists/${data.message}`;
        axios.get(url)
        .then(function (response)
        {
            is_valid = response.data["result"];
            console.log(is_valid);
            let index = round_places.length;
            while (index--) {
                if (data.message == round_places[index]){
                    round_repeated = true;
                }
            }
            if( is_valid && !round_repeated){
                round_places.push(data.message);
            } else {
                let p2 = document.querySelector("#chat-th").lastChild.innerText;
                socket.send(JSON.stringify({
                    'message': p2 + " Won!",
                    'username': userName,
                    'room': roomName,
                }))
                console.log("GAME OVER");
                socket.close();
            }
        })

    } else {
        alert('The message was empty');
    }
    round += 1;
};
socket.onclose= event => {
    console.log("Closed");
};

document.querySelector("#submit").onclick = function(e){
    e.preventDefault();
    const messageInputDom = document.querySelector("#chat-message");
    const message = messageInputDom.value;
    if (last_char_p2){
        console.log(last_char_p2, message[0]);
        if (last_char_p2 === message[0]){
            socket.send(JSON.stringify({
                'message': message,
                'username': userName,
                'room': roomName,
            }))
            messageInputDom.value = '';
        } else {
            let p2 = document.querySelector("#chat-th").lastChild.innerText;
            socket.send(JSON.stringify({
                'message': p2 + " Won!",
                'username': userName,
                'room': roomName,
            }))
            console.log("GAME OVER");
            socket.close();
        }
    } else {
        socket.send(JSON.stringify({
            'message': message,
            'username': userName,
            'room': roomName,
        }))
    }
}

