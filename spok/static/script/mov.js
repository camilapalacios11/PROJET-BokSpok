// script.js

const cards = document.querySelectorAll('.card');
const lists = document.querySelectorAll('.list');

// Añadir un identificador único a cada tarjeta
cards.forEach((card, index) => {
  card.setAttribute('id', 'card-' + index);
  card.addEventListener('dragstart', dragStart);
});

lists.forEach(list => {
  list.addEventListener('dragover', dragOver);
  list.addEventListener('drop', drop);
});

function dragStart(e) {
  e.dataTransfer.setData('text/plain', e.target.id);
}

function dragOver(e) {
  e.preventDefault();  // Esto permite que el elemento se pueda soltar aquí
}

function drop(e) {
  e.preventDefault();
  const id = e.dataTransfer.getData('text/plain');
  const card = document.getElementById(id);

  if (card) {
    e.target.appendChild(card);  // Mueve la tarjeta al contenedor de destino
    enviar("hecho", card.id);
    console.log(e.target.id);
  }
}

function enviar(estado, id){
    fetch('http://localhost:8000/tareas', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({estado: estado, id: id})
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log('Error:', error));
    }



    function toggleSelection(button, email) {
      event.preventDefault(); // Evita el submit
      const selectedInput = document.getElementById("selected_users");
      let selectedUsers = selectedInput.value ? selectedInput.value.split(",") : [];
  
      // Verifica si el usuario ya está seleccionado
      if (selectedUsers.includes(email)) {
        // Si ya está seleccionado, lo quitamos
        selectedUsers = selectedUsers.filter(user => user !== email);
        button.style.backgroundColor = ""; // Restablecer estilo
      } else {
        // Si no está seleccionado, lo añadimos
        selectedUsers.push(email);
        button.style.backgroundColor = "green"; // Marcar como seleccionado
      }
  
      // Actualizamos el valor del campo oculto
      selectedInput.value = selectedUsers.join(",");
    }    

    // cuanndo la pag se carga
// TODO SOBRE MI WEB SOKE

$(function(){

  console.log(nombre, sala_id)

  var protocol = window.location.protocol === "https:" ? "wss://" : "ws://";
  var url = protocol + window.location.host + '/ws/mostrar_sala/' + sala_id + '/';
  console.log("mi url -------------------------")
  console.log(url)
  var chatSocket = new WebSocket(url)

  // Definimos un tiempo de desconexión de 5 minutos (en milisegundos)
  console.log(chatSocket)

  chatSocket.onopen = function(e){
      console.log('WEBSOCKET ABIERTO')
  }

  chatSocket.onclose = function(e){
      console.log('WEBSOCKET CERRADO')
  }

  // Agregar eventos al botón y al input
  document.querySelector("#btnMensaje").addEventListener("click", sendMensaje);

  document.querySelector("#inpMensaje").addEventListener("keypress", function(e) {
    if (e.keyCode === 13) {
      sendMensaje();
    }
  });

  // Función para enviar el mensaje
  function sendMensaje() {
    console.log("En función mensaje");
    var mensa = document.querySelector("#inpMensaje");

    // Cargar mensaje en HTML si el campo no está vacío
    if (mensa.value.trim() !== "") {
      loadMensajeHTML(mensa.value.trim());
      mensa.value = ""; // Limpiar el campo de texto
    }
  }

  // Función para cargar el mensaje en HTML
  function loadMensajeHTML(m) {
    const now = new Date();
    const horaFecha = now.toLocaleString(); // Obtener hora y fecha actuales

    document.querySelector(".box_mensaje").innerHTML += `
      <div class="alert alert-danger" role="alert">
        ${m}
        <div>
          <small class="fst-italic fw-bold"> ${nombre} ${apellido} </small>
          <small class="float-end">${horaFecha}</small>
        </div>
      </div>
    `;
  }
});



// TODO SOBRE MI MODAL WAA

const modal = document.getElementById("myModal");
const openModal = document.getElementById("openModal");
const closeModal = document.querySelector(".close");

// Abrir el modal
openModal.addEventListener("click", () => {
  modal.style.display = "block";
});

// Cerrar el modal al hacer clic en la "X"
closeModal.addEventListener("click", () => {
  modal.style.display = "none";
});

// Cerrar el modal al hacer clic fuera del contenido
window.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
});


// faking canvas 
const canvas = new fabric.Canvas('canvas');

// Configuración inicial
canvas.isDrawingMode = false; // Comienza sin el lápiz activado
