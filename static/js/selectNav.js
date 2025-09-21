export async function selectNavItems() {
  document.addEventListener('DOMContentLoaded',  async function (e) {
    e.preventDefault();
    const currLocation = this.location.pathname;
    await setSubMenus(currLocation.split('/')[1]);

    document.querySelectorAll(".sub-url").forEach(item => {
      if (currLocation == item.getAttribute('href') && currLocation.split('/').length > 3){
        item.style.backgroundColor = 'rgba(5, 79, 216, 1)';
        const parentNode =item.parentElement?.parentElement?.parentElement?.firstElementChild;
        parentNode.style.color = 'rgba(188, 211, 253, 1)';
        parentNode.style.backgroundColor = 'rgba(0, 60, 172, 1)';
        parentNode.style.border='1px solid rgba(0, 34, 95, 1)';
      }
  });
  });
}

async function loadByFile(file_uri) {
  await fetch(file_uri)
    .then(response => response.text())
    .then(data => {
      const sub_menu = document.querySelector('.sub-menu')
      sub_menu.innerHTML = data
    })
}
async function setSubMenus(item){
  document.querySelectorAll(".navbar-btn").forEach(item => {
    item.classList.remove('curr-url');
  });
  document.querySelector('#'+item).classList.add('curr-url');
  switch (item) {
    case 'python':
      await loadByFile('/static/nav-html/_python-nav.html');
      break;
    case 'java':
      await loadByFile('/static/nav-html/_java-nav.html');
      break;
    case 'spring':
      await loadByFile('/static/nav-html/_spring-nav.html');
      break;
    case 'database':
      await loadByFile('/static/nav-html/_database-nav.html');
      break;
    case 'apps':
      await loadByFile('/static/nav-html/_apps-nav.html');
      break;
    case 'javascript':
      await loadByFile('/static/nav-html/_javascript-nav.html');
      break;
    case 'dom':
      await loadByFile('/static/nav-html/_dom-nav.html');
      break;                
    default:
      await loadByFile('/static/nav-html/_home-nav.html');
      break;
  }
}