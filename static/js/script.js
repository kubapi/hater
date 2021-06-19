$(document).ready(function() {
    $('#ranking_table').DataTable({
        "paging":   false,
        "info":     false,
        "ordering": false,
        language: { 
            "search": "Znajdź swój wynik:",
            "zeroRecords": "Niestety... pusto!",
        },

        //add these config to remove empty header
        "bJQueryUI": true,
        "sDom": 'lfrtip'
    });
} );

// Tinder cards (credits to https://codepen.io/RobVermeer/pen/japZpY)

var tinderContainer = document.querySelector('.tinder');
var allCards = document.querySelectorAll('.tinder--card');
var nope = document.getElementById('reject');

function initCards(card, index) {
  var newCards = document.querySelectorAll('.tinder--card:not(.removed)');

  newCards.forEach(function (card, index) {
    card.style.zIndex = allCards.length - index;
    card.style.transform = 'scale(' + (20 - index) / 20 + ') translateY(-' + 30 * index + 'px)';
    card.style.opacity = (10 - index) / 10;
  });
  
  tinderContainer.classList.add('loaded');
}

initCards();

allCards.forEach(function (el) {
  var hammertime = new Hammer(el);

  hammertime.on('pan', function (event) {
    el.classList.add('moving');
    document.getElementById("blur-0").style.filter = "blur(2px)";
    document.getElementById("blur-1").style.filter = "blur(2px)";

  });

  hammertime.on('pan', function (event) {
    if (event.deltaX === 0) return;
    if (event.center.x === 0 && event.center.y === 0) return;

    if (nope !== null) {
      if (event.deltaX < 0) {
        tinderContainer.classList.toggle('tinder_nope', event.deltaX < 0);
        $("#reject").show()
        $("#accept").hide()
      }
      if (event.deltaX > 0) {
        tinderContainer.classList.toggle('tinder_love', event.deltaX > 0);
        $("#accept").show()
        $("#reject").hide()
      }
    } else {
      $("#accept").show()
      $("#reject").hide()
      tinderContainer.classList.toggle('tinder_love', event.deltaX !== 0);
    }

    var xMulti = event.deltaX * 0.05;
    var yMulti = event.deltaY / 90;
    var rotate = xMulti * yMulti;

    event.target.style.transform = 'translate(' + event.deltaX + 'px, ' + event.deltaY + 'px) rotate(' + rotate + 'deg)';
  });

  hammertime.on('panend', function (event) {
    el.classList.remove('moving');

    document.getElementById("blur-0").style.filter = "none";
    document.getElementById("blur-1").style.filter = "none";

    tinderContainer.classList.remove('tinder_love');
    tinderContainer.classList.remove('tinder_nope');
    
    var moveOutWidth = document.body.clientWidth;
    var keep = Math.abs(event.deltaX) < 60 || Math.abs(event.velocityX) < 0.5;

    event.target.classList.toggle('removed', !keep);

    if (keep) {
      event.target.style.transform = '';
    } else {
      if (event.deltaX > 0) {
        $("#accept-choice").click()
      } 
      else if (event.deltaX < 0) {
        if (nope !== null) {
          $("#reject-choice").click()
        } else {
          $("#accept-choice").click()
        }
      }
      var endX = Math.max(Math.abs(event.velocityX) * moveOutWidth, moveOutWidth);
      var toX = event.deltaX > 0 ? endX : -endX;
      var endY = Math.abs(event.velocityY) * moveOutWidth;
      var toY = event.deltaY > 0 ? endY : -endY;
      var xMulti = event.deltaX * 0.03;
      var yMulti = event.deltaY / 80;
      var rotate = xMulti * yMulti;

      event.target.style.transform = 'translate(' + toX + 'px, ' + (toY + event.deltaY) + 'px) rotate(' + rotate + 'deg)';
      initCards();
    }
  });
});