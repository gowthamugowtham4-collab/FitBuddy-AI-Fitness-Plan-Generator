document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll("form");
  forms.forEach(form => {
    form.addEventListener("submit", () => {
      const button = form.querySelector("button[type='submit']");
      if (button && !form.action.includes("/delete-user/")) {
        button.disabled = true;
        button.textContent = "Processing…";
      }
    });
  });
});
