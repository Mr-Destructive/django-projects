let tab = document.getElementById("tab");
let row;
let rowcount = 0;
let points,com,ply;
let win = document.querySelector(".alert");
let pointdiv = document.querySelector(".points");
let info = document.querySelector("#info");
let placeinp = document.querySelector("#place");
let start = document.getElementById("start");
let submit = document.getElementById("submit");
let botlast;
placeinp.disabled=true;
submit.disabled=true;

document.getElementById("submit").addEventListener("click",()=>{

    placeinp.disabled=true;
    plyplace= placeinp.value;	
    if(plyplace == ''){
        placeinp.disabled=false;
    }
    else{
    plyplace=plyplace.toLowerCase();

    validate(plyplace, ()=> {
    
    row = tab.insertRow(rowcount);
    if(toss === 0){
        ply = row.insertCell(0);
    }
    else{
        com = row.insertCell(0);
        ply = row.insertCell(1);
    }
        ply.innerHTML = plyplace;
        placeinp.value = "";
        scroller();
        plylast = getLast(plyplace);
        botplace = givePlace(plylast);
        botlast = getLast(botplace);
        submit.disabled=false;
    })
    }
});

document.getElementById("place").addEventListener("keyup",function(event){
	if(event.keyCode === 13){
		event.preventDefault();
		document.getElementById("submit").click();
	}});
document.querySelector(".closebtn").addEventListener("click", () => {
    document.querySelector(".alert").style.display="none";
    document.querySelector(".closebtn").style.display="none";
})
let place="";
let a=[],b=[],c=[],e=[],f=[],d=[],g=[],h=[],i=[],j=[],k=[],l=[],m=[];
let n=[],o=[],p=[],q=[],r=[],s=[],t=[],u=[],v=[],w=[],x=[],y=[],z=[];
let valid = false;

coms = document.getElementById('tab');

observer = new MutationObserver(function(mutationsList, observer) {
    complast = getLast(place);
    if(points > 0){
    info.firstChild.nodeValue = "Enter a Place beginning with : " + complast;
    }
});

observer.observe(coms, {characterData: false, childList: true, attributes: false});

function scroller(){
	let scrop = document.getElementById('tab');
	scrop.scrollTop =scrop.scrollHeight;
}

function toss()
{
    start.innerHTML="Restart";
    start.style.top="28%";
    start.style.left="40%";
    win.style.visibility="hidden";
    document.querySelector(".closebtn").style.visibility="hidden";
    info.style.visibility="visible";
    placeinp.disabled=true;
    let toss=Math.floor(Math.random()*2);
    info.innerHTML='';
    var Parent = document.getElementById('tab');
    rowcount = 0;
    points=0;
    pointdiv.innerHTML = "Points : " + points;
    while(Parent.hasChildNodes())
    {
       Parent.removeChild(Parent.firstChild);
    }
    a=[],b=[],c=[],e=[],f=[],d=[],g=[],h=[],i=[],j=[],k=[],l=[],m=[];
    n=[],o=[],p=[],q=[],r=[],s=[],t=[],u=[],v=[],w=[],x=[],y=[],z=[];
    tab = document.getElementById("tab");
    row = tab.insertRow(0);
    com = row.insertCell(0);
    rowcount = 0;
    play(toss);
    
}

function play(toss)
{
    if( toss === 0)
    {
        info.innerHTML='The Bot enters the place first';
        placeinp.disabled=true;
        let letter ="abcdefghijklmnopqrstuvwxyz";
		let random_index=Math.floor(Math.random()*26);
		let random_char=letter[random_index];
		botplace=givePlace(random_char);
    }
    else{
        info.innerHTML='You will enter the place first';
        placeinp.disabled=false;
    }
    submit.disabled=false;
}

// gets last character of the given place
function getLast(place)
{
    let last = place.length
    return place[last-1];
}

// random place generator for bot
function givePlace(letter)
{
    let url = "https://djangonaut.pythonanywhere.com/world-atlas/api/places/get/"+letter+"/";
    axios.get(url) 
    .then(function (response)
    {
        place = response["data"][letter];
        if(validate_comp(place)){
            rowcount+=1;
            com.appendChild(document.createTextNode(place));
            botlast=getLast(place);
            scroller();
            placeinp.disabled=false;
            info.firstChild.nodeValue = "Enter a Place beginning with : " + botlast;
        }
        return place;
    })
    .catch(function (error) {
        console.log(error);
    })
    return place;
}

//validate a user input place
function validate(place, _callback)
{
    let first = place[0];
    if(points !== 0 ){
        if(first !== botlast){
            last=1;
        }
    }
    let placelist = [];
    let exists = 0, repeated = 0, count = 0, last=0;
    let url = "https://djangonaut.pythonanywhere.com/world-atlas/api/places/exists/"+place;
    _callback(axios.get(url) 
    .then(function (response)
    {
    is_valid = response.data["result"];

    if( is_valid )
    {
        exists=1;
    }

    let dict = [];

    if(first == 'a') { dict = a; }
       
    if(first == 'b') { dict = b; }
       
    if(first == 'c') { dict = c; }
       
    if(first == 'd') { dict = d; }
       
    if(first == 'e') { dict = e; }
       
    if(first == 'f') { dict = f; }
       
    if(first == 'g') { dict = g; }
       
    if(first == 'h') { dict = h; }
       
    if(first == 'i') { dict = i; }
       
    if(first == 'j') { dict = j; }
       
    if(first == 'k') { dict = k; }
       
    if(first == 'l') { dict = l; }
       
    if(first == 'm') { dict = m; }
       
    if(first == 'n') { dict = n; }
       
    if(first == 'o') { dict = o; }
       
    if(first == 'p') { dict = p; }
       
    if(first == 'q') { dict = q; }
       
    if(first == 'r') { dict = r; }
       
    if(first == 's') { dict = s; }
       
    if(first == 't') { dict = t; }
       
    if(first == 'u') { dict = u; }
       
    if(first == 'v') { dict = v; }
       
    if(first == 'w') { dict = w; }
       
    if(first == 'x') { dict = x; }
       
    if(first == 'y') { dict = y; }
       
    if(first == 'z') { dict = z; }

    let dictlen =dict.length;

    for(let i=0; i<dictlen; i++)
    {
        if(place == dict[i])
        {
            repeated=1;
            break;
        }
        else
        {
            count+=1;
        }
    }
    
    if(exists == 1 && count == dictlen && repeated == 0 && last == 0){
        valid=true;
        add_to_list(place);
        placeinp.disabled=false;
        submit.disabled=false;
        placeinp.focus();
        points+=1;
        pointdiv.innerHTML = "Points : " + points;
    }

    else{
        valid=false;
        placeinp.disabled=true;
        submit.disabled=true;
        win.innerHTML="You Lost";
        win.style.backgroundColor="#ff4436";
        win.style.visibility="visible";
        document.querySelector(".closebtn").style.visibility="visible";
        info.style.visibility="hidden";
        start.style.top= "75%";
        start.innerHTML= "Restart";
        start.style.visibility="visible";
    }
    return valid;
    })
    .catch(function (error) {
        console.log(error);
    }))
    
}

function validate_comp(place)
{
    let first = place[0];
    let repeated = 0, count = 0;
    let dict = [];

    if(first == 'a') { dict = a; }
       
    if(first == 'b') { dict = b; }
       
    if(first == 'c') { dict = c; }
       
    if(first == 'd') { dict = d; }
       
    if(first == 'e') { dict = e; }
       
    if(first == 'f') { dict = f; }
       
    if(first == 'g') { dict = g; }
       
    if(first == 'h') { dict = h; }
       
    if(first == 'i') { dict = i; }
       
    if(first == 'j') { dict = j; }
       
    if(first == 'k') { dict = k; }
       
    if(first == 'l') { dict = l; }
       
    if(first == 'm') { dict = m; }
       
    if(first == 'n') { dict = n; }
       
    if(first == 'o') { dict = o; }
       
    if(first == 'p') { dict = p; }
       
    if(first == 'q') { dict = q; }
       
    if(first == 'r') { dict = r; }
       
    if(first == 's') { dict = s; }
       
    if(first == 't') { dict = t; }
       
    if(first == 'u') { dict = u; }
       
    if(first == 'v') { dict = v; }
       
    if(first == 'w') { dict = w; }
       
    if(first == 'x') { dict = x; }
       
    if(first == 'y') { dict = y; }
       
    if(first == 'z') { dict = z; }

    let dictlen =dict.length;

    for(let i=0; i<dictlen; i++)
    {
        if(place == dict[i])
        {
            repeated=1;
            break;
        }
        else
        {
            count+=1;
        }
    }

    if(count === dictlen && repeated === 0){
        valid=true;
        add_to_list(place);
    }

    else{
        placeinp.disabled=true;
        info.innerHTML = "You Won!!";
        win.style.backgroundColor = "#00dd14";
        win.innerHTML="You Won!"
        win.style.visibility="visible";
        document.querySelector(".closebtn").style.visibility="visible";
        start.style.top= "75%";
        start.innerHTML= "Restart";
        start.style.visibility="visible";
        info.style.visibility = "hidden";
        valid=false;
    }
    return valid;
}

// add a valid place to dicts
function add_to_list(place)
{
   if ( place[0] == 'a' )
   { a.push(place); }

   if ( place[0] == 'b' )
   { b.push(place); }

   if ( place[0] == 'c' )
   { c.push(place); }

   if ( place[0] == 'd' )
   { d.push(place); }

   if ( place[0] == 'e' )
   { e.push(place); }

   if ( place[0] == 'f' )
   { f.push(place); }

   if ( place[0] == 'g' )
   { g.push(place); }

   if ( place[0] == 'h' )
   { h.push(place); }

   if ( place[0] == 'i' )
   { i.push(place); }

   if ( place[0] == 'j' )
   { j.push(place); }

   if ( place[0] == 'k' )
   { k.push(place); }

   if ( place[0] == 'l' )
   { l.push(place); }

   if ( place[0] == 'm' )
   { m.push(place); }

   if ( place[0] == 'n' )
   { n.push(place); }

   if ( place[0] == 'o' )
   { o.push(place); }

   if ( place[0] == 'p' )
   { p.push(place); }

   if ( place[0] == 'q' )
   { q.push(place); }

   if ( place[0] == 'r' )
   { r.push(place); }

   if ( place[0] == 's' )
   { s.push(place); }

   if ( place[0] == 't' )
   { t.push(place); }

   if ( place[0] == 'u' )
   { u.push(place); }

   if ( place[0] == 'v' )
   { v.push(place); }

   if ( place[0] == 'w' )
   { w.push(place); }

   if ( place[0] == 'x' )
   { x.push(place); }

   if ( place[0] == 'y' )
   { y.push(place); }

   if ( place[0] == 'z' )
   { z.push(place); }

}
