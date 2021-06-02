// Función para enlazar los selects
const $carro = $("#car_id");
const $modelo = $("#car_model_id");
const $motor = $("#engine_id");

$carro.change(function(){
    $modelo.val('');
    
    $modelo.prop('disabled', !Boolean($carro.val()));
    $motor.prop('disabled', !Boolean($modelo.val()));
    $modelo.find('option[data-carro]').hide();
    $modelo.find('option[data-carro="' + $carro.val() + '"]').show();
    
});

$modelo.change(function(){
    $motor.val('');
    
    $motor.prop('disabled', !Boolean($modelo.val()));
    $modelo.prop('disabled', !Boolean($carro.val()));
    $motor.find('option[data-carro]').hide();
    $motor.find('option[data-carro="' + $modelo.val() + '"]').show();
    
});

// Funcion filtrar
$(document).ready(function(){
    $("#myInput").on("keyup",function(){                                // Cuando se teclea algo
        var value = $(this).val().toLowerCase();                        // Toma el valor del input en minuscula
        $("#myTable tr").filter(function(){                             // 
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        })
    })
});


// Generar PDF desde HTML
function generatePDF(){
    const element = document.getElementById("invoice");
    $('#invoice tr > *:nth-child(6)').hide();
    var opt = {
        margin:       1,
        filename:     'report.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        enableLinks:  false,
        pagebreak:    {mode: "avoid-all"},
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
      };
    html2pdf()
    .set(opt)
    .from(element)
    .save();
}

function viewPDF(){
    const element = document.getElementById("invoice");
    $('#invoice tr > *:nth-child(6)').hide();
    var opt = {
        margin:       1,
        filename:     'report.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        enableLinks:  true,
        pagebreak:    {mode: "avoid-all"},
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
      };
    html2pdf()
    .set(opt)
    .from(element);
    
    html2pdf().set(opt).from(element).toPdf().get('pdf').then(function (pdf) {
        window.open(pdf.output('bloburl'), '_blank');
      });
}

// Función para que los checkboxes se seleccionen todos

function toggle(source,toAdd) {
    checkboxes = document.getElementsByName(toAdd);
    for (var i = 0,
        n = checkboxes.length; i < n; i++) {
        checkboxes[i].checked = source.checked;
    }
}

function toggle(source,toDel) {
    checkboxes = document.getElementsByName(toDel);
    for (var i = 0,
        n = checkboxes.length; i < n; i++) {
        checkboxes[i].checked = source.checked;
    }
}


// Boton defaul para que reinicie la tabla
document.getElementById("default").addEventListener("click",function(){
    $('#invoice tr > *:nth-child(6)').show();
    $('#invoice tr > *:nth-child(1)').show();
})
// boton para exportar a Excel
document.getElementById("downloadexcel").addEventListener("click",function(){
    $('#invoice tr > *:nth-child(6)').hide();
    $('#invoice tr > *:nth-child(1)').hide();
    var table2excel = new Table2Excel();
    table2excel.export(document.querySelectorAll("#invoice"));
    location.reload();
})