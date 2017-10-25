$(document).ready(function(){
    console.log("Hello, World!");
    $("input[type='password']").change(function(){
        if($("#pw").val() != $("#pwc").val())
        {
            $("#pwnomatch").show();
            $("#regbutton").attr("disabled", true);
        }
        else
        {
            $("#pwnomatch").hide();
            $("#regbutton").attr("disabled", false);
        }
    });
});