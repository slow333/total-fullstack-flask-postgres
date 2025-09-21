export async function selectNavItems() {
  // document.addEventListener('DOMContentLoaded',  function () {
    const menuItems = document.querySelectorAll('.navbar-btn');
      menuItems.forEach( menuItem => {
      menuItem.addEventListener('click',async function (e) {
        e.preventDefault();
        switch (menuItem.id) {
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
        const selectedItems = document.querySelectorAll("#python, #java, #spring, #database, #apps, #javascript, #dom");
        selectedItems.forEach(item => {
          item.classList.remove('active');
        });
        menuItem.classList.add('active');
      })
    })
  // });
}

async function loadByFile(file_uri) {
  await fetch(file_uri)
    .then(response => response.text())
    .then(data => {
      const sub_menu = document.querySelector('.sub-menu')
      sub_menu.innerHTML = data
    })
}  