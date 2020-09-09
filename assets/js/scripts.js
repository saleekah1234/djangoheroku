// main animation
$(".cta").click(function () {
  $(".transition").toggleClass("anim-trans");
  setTimeout(function () {
    window.location.href = "#order";
  }, 3500);
});

// on scroll background animation
$(window).scroll(function () {
  if ($(this).scrollTop() > window.innerHeight - 100) {
    $(".transition").addClass("hidden");
    $(".about").addClass("bg-color");
  } else {
    $(".transition").removeClass("hidden");
    $(".transition").addClass("visible");
    $(".transition").fadeIn(1000);
    $(".about").removeClass("bg-color");
  }
  if ($(this).scrollTop() > window.innerHeight * 3 - 100) {
    $(".order").addClass("bg-color");
  } else {
    $(".order").removeClass("bg-color");
  }
});
//  navigation active class functionality
$(".nav-link").on("click", (event) => {
  $(".navbar-nav").find(".active").removeClass("active");
  $(event.target).parent().addClass("active");
});

$(document).ready(function () {
  $('a[href="' + location.pathname + '"]')
    .closest(".nav-item")
    .addClass("active");
});

// header hide on scroll
$(document).ready(function () {
  var banner_height = $("#mynav").height();
  var lastScrollTop = 0;
  $(window).scroll(function () {
    var scroll = $(window).scrollTop();
    var currScrollTop = $(this).scrollTop();
    if (currScrollTop > 0) {
      $("#mynav").css("background", "#fff");
    } else {
      $("#mynav").css("background", "transparent");
    }
    if (scroll >= banner_height && currScrollTop > lastScrollTop) {
      $("#mynav").slideUp();
    } else {
      $("#mynav").slideDown();
    }
    lastScrollTop = currScrollTop;
  });
});
