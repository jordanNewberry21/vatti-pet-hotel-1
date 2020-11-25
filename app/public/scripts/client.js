$(function () {
  //on ready func using anonymous function
});

function getPets() { // ajax GET function
  $.ajax({
    method: 'GET',
    url: '/pets' // setting the url for data transactions
  }).then(function (response) {
    console.log(response);
    renderPets(response); // call render with response from server
  }).catch(function (error) {
    console.log('error in GET route', error);
  });
};

// POST request  
function addPet() { 
  console.log('adding pet')
  $.ajax({
    method: 'POST', 
    url: '/pets', 
    data: { 
      name: $('#petNameInput').val(), 
      breed: $('#breedInput').val(), 
      color: $('#colorInput').val(), 
      notes: $('#petNotesInput').val() 
      }
}).then( function(response) {
  console.log('pets posted') 
})

//  DELETE Request 
function deletePet( petId ) {
  $.ajax({
    method: 'DELETE',
    url: `/pets/${petId}`
  })
    .then(function (response) {
      getKoalas();
    })
    .catch(function (error) {
      console.log('Error:', error);
      alert('Something bad happened. Try again later');
    })
}

function checkInStatus(petId, petCheckIn) {
  console.log (`koalaInfo in fn - id: ${petId} Check in status: ${petCheckIn}`);
  $.ajax({
    method: 'PUT',
    url: `/pets/${petId}`,
    data: petCheckIn
  })
    .then(function (response) {
      getKoalas();
    })
    .catch(function (error) {
      console.log('Error:', error);
      alert('Something bad happened. Try again later');
    })
}
// Render pets 
function renderPets(petData) {
  let display = $('#petTables');
  display.empty();
  for (pet of petData) {
    let $tr = $(`<tr data-id='${pet.id}'</tr>`);
    $tr.data('pet', pet);
    $tr.append(`<td class="name" data-name='${pet.name}'>${pet.name}</td>`);
    $tr.append(`<td class="breed">${pet.breed}</td>`);
    $tr.append(`<td class="color">${pet.color}</td>`);
    $tr.append(
      `<td class="checkIn" data-checkIn='${pet.checked_in}'>${pet.checked_in}</td>`
    );
    $tr.append(`<td class="notes">${pet.notes}</td>`);
    $tr.append(
      `<td class="td-checkIn"><button class='btn-checkIn'>Mark For checkIn</button></td>`
    );
    $tr.append(
      `<td class="td-delete"><button class='btn-delete'>Delete</button></td>`
    );
    display.append($tr);
  }
}