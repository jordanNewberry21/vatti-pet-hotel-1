$(function () {
  console.log('in ready function');
  getPets();
  $('#petTableSpot').on('click', '.btn-delete', deletePet);
  $('#petSubmitBtn').on('click', addPet);
  //on ready func using anonymous function
});

function getPets() {
  // ajax GET function
  $.ajax({
    method: 'GET',
    url: '/pets', // setting the url for data transactions
  })
    .then(function (response) {
      renderPets(response); // call render with response from server
    })
    .catch(function (error) {
      console.log('error in GET route', error);
    });
}

// POST request
function addPet(e) {
  e.preventDefault();
  console.log('adding pet');
  let pet = {
    name: $('#petNameInput').val(),
    breed: $('#breedInput').val(),
    color: $('#colorInput').val(),
    notes: $('#petNotesInput').val(),
  };
  $.ajax({
    method: 'POST',
    contentType: 'application/json',
    url: '/pets',
    dataType: 'json',
    data: pet,
  }).then(function (response) {
    console.log('pets posted');
  });
}

//  DELETE Request
function deletePet() {
  let petId = $(this).closest('tr').data('id');
  console.log('in delete-btn. pet id is... ', petId);
  $.ajax({
    method: 'DELETE',
    url: `/pets/${petId}`,
  })
    .then(function (response) {
      getPets();
    })
    .catch(function (error) {
      console.log('Error:', error);
      alert('Something bad happened. Try again later');
    });
}

function checkInStatus(petId, petCheckIn) {
  console.log(`pet Info in fn - id: ${petId} Check in status: ${petCheckIn}`);
  $.ajax({
    method: 'PUT',
    url: `/pets/${petId}`,
    data: petCheckIn,
  })
    .then(function (response) {
      getPets();
    })
    .catch(function (error) {
      console.log('Error:', error);
      alert('Something bad happened. Try again later');
    });
}
// Render pets
function renderPets(petData) {
  let display = $('#petTableSpot');
  pets = petData.pets;
  display.empty();
  for (pet of pets) {
    console.log(pet);
    let $tr = $(`<tr data-id='${pet[0]}'</tr>`);
    $tr.data('pet', pet);
    $tr.append(`<td class="name" data-name='${pet[1]}'>${pet[1]}</td>`);
    $tr.append(`<td class="breed">${pet[2]}</td>`);
    $tr.append(`<td class="color">${pet[3]}</td>`);
    $tr.append(`<td class="checkIn" data-checkIn='${pet[4]}'>${pet[4]}</td>`);
    $tr.append(`<td class="notes">${pet[5]}</td>`);
    $tr.append(
      `<td class="td-checkIn"><button class='btn-checkIn'>Mark For checkIn</button></td>`
    );
    $tr.append(
      `<td class="td-delete"><button class='btn-delete'>Delete</button></td>`
    );
    display.append($tr);
  }
}
