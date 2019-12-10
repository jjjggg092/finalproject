document.addEventListener('DOMContentLoaded', () => {
  tips();
});

/*-----  Side navbar in principal/base.html-----*/
function openNav() {
    document.getElementById("sideNavigation").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
    document.getElementById("sideNavigation").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}


function showAdd() {
  var show = document.querySelector('.add');
  var hide1 = document.querySelector('.waste');
  var hide2 = document.querySelector('.summary');
  show.style.display = 'block';
  hide1.style.display = 'None';
  hide2.style.display = 'None';
  closeNav();
  tips()
}
function showRemove() {
  var hide1 = document.querySelector('.add');
  var show = document.querySelector('.waste');
  var hide2 = document.querySelector('.summary');
  show.style.display = 'block';
  hide1.style.display = 'None';
  hide2.style.display = 'None';
  closeNav();
  tips()
}

function showBrief() {
  var hide1 = document.querySelector('.add');
  var hide2 = document.querySelector('.waste');
  var show = document.querySelector('.summary');
  show.style.display = 'block';
  hide1.style.display = 'None';
  hide2.style.display = 'None';
  closeNav();
  tips()
}

function tips() {
  var tips = [
    "The first step to start saving money is to figure out how much you spend. Keep track of all your expenses—that means every coffee, household item and cash tip.",
    "Use resources such as community event listings to find free or low-cost events to reduce entertainment spending.",
    "Cancel subscriptions and memberships you don’t use—especially if they renew automatically.",
    "Commit to eating out only once a month and trying places that fall into the “cheap eats” category.",
    "Give yourself a “cooling off period”: When tempted by a nonessential purchase, wait a few days. You may be glad you passed—or ready to save up for it.",
    "Almost all banks offer automated transfers between your checking and savings accounts. You can choose when, how much and where to transfer money or even split your direct deposit so a portion of every paycheck goes directly into your savings account."
  ];
  var index = Math.round((Math.random() * 100) % (tips.length -1));
  document.querySelector('#tip').innerHTML = tips[index];
}
