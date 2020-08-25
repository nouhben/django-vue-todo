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
        tasks: [],
    },
    //use hooks to call the function at the event of page loaded
    created() {
        const vue_instance_ref = this;
        const r = sendRequest('', 'get')
            .then(function (response) {
                // .then() ==>. is a promise somthing like Future in Flutter
                //we can not use 'this' here because it will refere to the annonymous function and not
                // to Vue instance so i save a reference to my vue instance in a variable berfore defining the function

                vue_instance_ref.tasks = response.data.tasks;

            });
    },
    // cahe based function the manpulates the already 
    // rendred data
    computed: {
        taskList() {
            function tasksComparator(taskA, taskB) {
                if (taskA.isDone > taskB.isDone) {
                    return 1;
                }
                if (taskA.isDone < taskB.isDone) {
                    return -1;
                }
                return 0;
            }
            return this.tasks.sort(tasksComparator);
        }
    },
    methods: {
        createNewTask() {
            const vue_instance_ref = this;
            const formData = new FormData();
            formData.append('title', this.task);
            sendRequest('', 'post', formData)
                .then(function (response) {
                    vue_instance_ref.tasks.push(response.data.newTask);
                    // add the added task to the tasks
                    vue_instance_ref.task = '';
                    //clear the input
                });
        },
        taskAsDone(id, index) {
            const vm = this;
            sendRequest('' + id + '/done/', 'POST')
                .then(function (response) {
                    vm.tasks.splice(index, 1);
                    vm.tasks.push(response.data.taskCompleted);
                });
        },
        deleteTask(id, index) {
            const vm = this;
            sendRequest('' + id + '/delete/', 'POST')
                .then(function (response) {
                    vm.tasks.splice(index, 1);
                });
        },

    }
});