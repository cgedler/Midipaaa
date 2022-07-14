$(document).ready(function () {
    var table = $('#table').DataTable({
        responsive: true,
        "language": {
            url: "/static/js/location/es_ES.json"
        }
    });
});
function open_modal(url) {
    $('#myModal').load(url, function() {
        $(this).modal({
            backdrop: 'static',
            keyboard: false
        })
        $(this).modal('show');
        });
    return false;
}
function close_modal(){
    $('#myModal').modal('close');
    return false;
}
function delete_item() {
    var x = confirm("Desea Eliminar ?");
    if (x)
        return true;
    else
        return false;
}
