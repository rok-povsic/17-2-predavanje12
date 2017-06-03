$(document).ready(function() {
    var forma = $("#add-comment-form");
    forma.on("submit", function(e) {
        e.preventDefault();

        var url = forma.attr("action");
        var params = {
            csrf_token: $("input[name=csrf_token]").val(),
            text: $("textarea[name=text]").val()
        };
        $.post(url, params, function() {
            console.log("dobili smo POST odgovor");
            $(".comment").last().after(
                `
                <div class="panel panel-info comment" style="margin: 4px 25px">
      <div class="panel-body">
        <p>
          ` + params["text"] + `
        </p>
      </div>
    </div>
                `);
        });
    });
});