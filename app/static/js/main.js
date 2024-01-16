
var editor = new DataTable.Editor({
    ajax: 'http://127.0.0.1:8000/get-patients/',
    fields: [
        
        {
            label: 'First name:',
            name: 'rut'
        },
        {
            label: 'Last name:',
            name: 'name'
        },
        {
            label: 'Position:',
            name: 'age'
        },
        {
            label: 'Position:',
            name: 'medical_history'
        },
        
        {
            label: 'Position:',
            name: 'diet'
        },
        
        {
            label: 'Position:',
            name: 'smoker'
        },
        {
            label: 'Position:',
            name: 'height_weight'
        },
        
        {
            type: "select",
            label: 'Position:',
            name: 'patient_type',
            options: [
                {label:'Niño', value:1},
                {label:'Joven', value:2},
                {label:'Adulto', value:1},
            ]
        },
        
    ],
    table: '#example'
});
$(document).ready(function(){
    $('#example').DataTable();
     
    $('#submit').on('click', function(){
        $rut = $('#rut').val();
        $name = $('#name').val();
        $age = $('#age').val();
        $medical_history = $('#medical_history').val();
        $diet = $('#diet').val();
        $smoker = $('#smoker').val();
        $patient_type = $('#patient_type').val();
  
        if($rut == "" || $name == "" || $age == "" || $medical_history == "" || $medical_history=="" ||$diet=="" || $smoker=="" || $patient_type=="" ){
            alert("Please complete field");
        }else{
            $.ajax({
                type: "POST",
                url: "insert",
                data:{
                    rut: $rut,
                    name: $name,
                    age: $age,
                    medical_history: $medical_history,
                    diet: $diet,
                    smoker: $smoker,
                    patient_type: $patient_type,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    alert('Save Data');
                    $('#rut').val('');
                    $('#name').val('');
                    $('#age').val('');
                    $('#medical_history').val('');
                    $('#diet').val('');
                    $('#smoker').val('');
                    $('#patient_type').val('');
                    window.location = "/";
                }
            });
        }
    });
});
 
new DataTable('#example', {
    ajax: {
        url: 'http://127.0.0.1:8000/get-patients/',
        dataSrc: ''
    },
    buttons: [
        { 
            extend: 'create', 
            editor, 
            formButtons: [{
                text: 'Alert',
                extend: 'selectedSingle',
                action: function (e, dt, node, config) {
                    // Immediately add `250` to the value of the salary and submit
                    console.log(editor.get('rut'))
                }
            }]
        },
        { extend: 'edit', editor },
        { 
            extend: 'remove', 
            editor, 
        }
    ],
    columns:[
        {data: 'rut'},
        {data: 'name'},
        {data: 'age'},
        {data: 'medical_history'},
        {data: 'diet'},
        {data: 'smoker'},
        {data: 'height_weight'},
        {data: 'patient_type'},

    ],
    dom: 'Bfrtip',
    select: true
});
