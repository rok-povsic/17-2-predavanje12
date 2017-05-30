$(document).ready(function() {
    console.log("Izpis preko JS.");
    var name = "Rok";

    if (name === "Rok") {
        console.log("Pozdravljeni, Rok.");
    } else {
        console.log("Pozdravljen, neznanec.");
    }

    function izpis(text) {
        console.log(text);
    }

    izpis("Klic funkcije izpis.");

    var seznam = ["ABC", 23, false];
    seznam.forEach(function(element) {
        console.log(element);
    });

    $("h1").css("color", "red");

    $("#testni-gumb").click(function() {
        console.log("Klik gumba");

        var glava = $("h1");
        glava.css("font-size", "20px");
        $("body").css("background-color", "green");
        glava.hide();
    });

    var gumb2 = $("#testni-gumb-2");
    gumb2.click(function() {
        console.log("klik drugega gumba");
        $("#testni-div").fadeToggle(200);
    });

    gumb2.mouseover(function() {
        $("#testni-div").addClass("panel panel-warning");
    });
    gumb2.mouseout(function () {
        $("#testni-div").removeClass("panel panel-warning");
    });

    $("#nalaganje").hide();

    $(".details-link").click(function() {
        var kliknjenaPovezava = $(this);
        var idTeme = kliknjenaPovezava.attr("id");

        $("#nalaganje").fadeIn(300);

        $.get("/api/topic/details/" + idTeme, function(data) {
            var parsedData = $.parseJSON(data);
            $("#naslov-teme").text(parsedData.title);
            $("#vsebina-teme").text(parsedData.content);
            $("#nalaganje").fadeOut(300);
        });
    });
});
