function sendRequest(url, methode, data) {
    const r = axios({
        url: url,
        method: methode,
        data: data,
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
            //to allow django recognizing this request as ajax request
        }
    });
    return r;
}
const app = new Vue({
    el: '#app',
    data: {
        task: '',
        tasks: [
            { title: 'Flutted & firebase' },
        ]
    },
    //use hooks to call the function at the event of page loaded
    created() {
        var my_vue_object = this;
        var r = sendRequest('', 'get')
            // .then() ==. is a promise somthing like Future in Flutter
            .then(function (response) {
                //we can not use 'this' here because it will refere to the annonymous function and not
                // to Vue instance so i save a reference to my vue instance in a variable berfore defining the function
                my_vue_object.tasks = response.data.tasks;
            });
    },
    methods: {
        createTask() {
            var my_vue_object = this;
            var formData = new FormData();
            //console.log(this.task);
            //formData.append('title', this.task);
            formData.append('title', this.task);
            console.log(formData.values);
            sendRequest('', 'post', formData)
                .then(function (response) {
                    my_vue_object.tasks.push(response.data.task);// add the added task to the tasks
                    my_vue_object.task = '';//clear the input
                });
        }
    }
});