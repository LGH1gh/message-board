<template>
    <div>
        <div v-if='this.NUID == 0'>
            <button @click='login'>登录</button>
        </div>
        <div v-else>
            欢迎，{{ username }}
        </div>
        <form @submit.prevent='add_board'>
            <input type='text' contenteditable='true' placeholder='题目' v-model='userTitle'>
            <input type='text' contenteditable='true' placeholder='留言' v-model='userMessage'>
            <input type='submit' value='提交'>
            <div v-if='this.alert == 1'>题目和留言不能为空</div>
            <div v-if='this.alert == 2'>您必须先登录，再留言</div>
        </form>
        <ul class='page'>
            <li v-for='n in this.totalNumber' class='board'>
                <board :MID='n' :NUID='1'></board>
            </li>
        </ul>
    </div>
</template>

<script>
import board from './board'
export default {
    name: 'pageData',
    data: function () {  
        return {
            username: '',
            totalNumber: 0,
            NUID: 0,
            userMessage: '',
            userTitle: '',
            alert: 0
        }
    },
    components: {
        board
    },
    mounted() {
        this.get_totalNumber()
    },
    methods: {
        get_totalNumber() {
            console.log(this.NUID)
            this.$http.get('http://192.168.55.33:8000/api/get_totalNumber')
                .then((response) => {
                    let res = response.data
                    if (res.error_num == 0) {
                        this.totalNumber = res.total
                        console.log(this.totalNumber)
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        get_params() {
            this.NUID = this.$route.params.NUID
            this.username = this.get_username(this.NUID)
        },
        add_board() {
            if (this.NUID == 0) {
                this.alert = 2
            } else if (this.userTitle == '' || this.userMessage == '') {
                this.alert = 1
            } else {
                console.log(this.NUID, this.userTitle, this.userMessage)
                this.$http.get('http://192.168.55.33:8000/api/add_board', {params: {UID: this.NUID, title: this.userTitle, message: this.userMessage}})
                    .then((response) => {
                        let res = response.data
                        if (res.error_num == 0) {
                            this.get_totalNumber()
                            console.log(this.totalNumber)
                        } else {
                            console.log(res.msg)
                        }
                })
            }
        },
        get_username(UID) {
            this.$http.get('http://192.168.55.33:8000/api/get_username', {params: {UID: UID}})
                .then((response) => {
                    let res = response.data
                    if (res.error_num == 0) {
                        this.username = res.username
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        login() {
            this.$router.push({
                name: 'login'
            })
        }
    },
    watch: {
        '$route': 'get_params'
    }
}
</script>

<style scoped>

</style>
