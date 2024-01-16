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
            label: 'Position:',
            name: 'patient_type'
        },
        
    ],
    table: '#example'
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
        { extend: 'remove', editor }
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
