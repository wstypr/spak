// form submit
const form = document.getElementById("kuesioner");
const url =
  "https://script.google.com/macros/s/AKfycbyMWY6SY_BL9Je0rZ3rkZhlQM7oRoyRP-2Xmh3wpev7DNjXxPnjyYtLt5psintMfhgY/exec";

form.addEventListener("submit", (e) => {
  let data = new FormData(form);
  e.preventDefault();

  console.log(data.get("nama"));
  console.log(data.get("opd"));

  fetch(url, { method: "POST", body: data })
    .then(function (response) {
      console.log(response);
      let msg = new bootstrap.Modal(document.getElementById("success-msg"));
      form.reset();
      msg.show();
    })
    .catch(function (error) {
      console.log(error);
      let msg = new bootstrap.Modal(document.getElementById("error-msg"));
      msg.show();
    });
});
