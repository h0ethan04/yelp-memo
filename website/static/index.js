function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/saved";
    });
  }

function saveNote(name, img, address, phone, url, rating, business_id) {
    fetch("/save-note", {
      method: "POST",
      body: JSON.stringify({ name: name,
                             img: img,
                             address: address,
                             phone: phone,
                             url: url,
                             rating: rating,
                             business_id: business_id})
    }).then((_res) => {
      if(_res.ok) {
        var snackbar = document.getElementById("snackbar");

        snackbar.className = "show";

        setTimeout(function(){snackbar.className = snackbar.className.replace("show", ""); }, 3000);
      }
    }

    //   window.location.href = '/saved'

    );
}


// function saveNote(name, img, address, phone, url) {
//   console.log(name, img, address, phone, url);
// }

// function clicked() {
//   console.log('button pressed');
// }