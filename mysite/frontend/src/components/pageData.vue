<template>
    <div class='page'>
        <div v-if='this.NUID > 0'>
            欢迎，{{ username }}
            <button @click='logout'>登出</button>
        </div>
        <div v-else>
            <button @click='login'>登录</button>
        </div>
        <form @submit.prevent='add_board'>
            <input type='text' contenteditable='true' placeholder='题目' v-model='userTitle'>
            <input type='text' contenteditable='true' placeholder='留言' v-model='userMessage'>
            <input type='submit' value='提交'>
            <div v-if='this.alert == 1'>题目和留言不能为空</div>
            <div v-if='this.alert == 2'>您必须先登录，再留言</div>
        </form>
        <ul class='page'>
            <li v-for='n in this.array' class='board'>
                <board :MID='n' :NUID='NUID'></board>
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
            alert: 0,
            array: []
        }
    },
    components: {
        board
    },
    created() {
        this.NUID = Number(sessionStorage.getItem('user'))
        console.log(sessionStorage.getItem('user'))
        if (!this.NUID) {
            this.NUID = 0
        }
    },
    mounted() {
        this.get_totalNumber()
        // this.NUID = this.$route.params.NUID
        // console.log(this.$route.params.NUID)
        console.log('Mounted')
        console.log(this.NUID)
        this.username = this.get_username(this.NUID)
        // console.log(this.NUID)
    },
    methods: {
        get_totalNumber() {
            // console.log(this.NUID)
            this.$http.get('http://localhost:8000/api/get_totalNumber')
                .then((response) => {
                    let res = response.data
                    if (res.error_num == 0) {
                        this.totalNumber = res.total
                        this.array = []
                        for (let i = this.totalNumber; i > 0; --i) {
                            this.methodByPush(i)
                        }
                        // console.log(array)
                        // console.log(this.array)
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        add_board() {
            if (this.NUID == undefined) {
                this.alert = 2
            } else if (this.userTitle == '' || this.userMessage == '') {
                this.alert = 1
            } else {
                console.log(this.NUID + this.userTitle + this.userMessage)
                this.$http.get('http://localhost:8000/api/add_board', {params: {UID: this.NUID, title: this.userTitle, message: this.userMessage}})
                    .then((response) => {
                        let res = response.data
                        if (res.error_num == 0) {
                            location.reload()
                            console.log('123')
                            // this.userMessage = ''
                            // this.userTitle = ''
                            // this.alert = 0
                            // this.get_totalNumber()
                            // console.log(this.totalNumber)
                        } else {
                            console.log(res.msg)
                        }
                })
            }
        },
        get_username(UID) {
            this.$http.get('http://localhost:8000/api/get_username', {params: {UID: UID}})
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
                path: '/login'
            })
        },
        logout() {
            this.$router.push({
                path: '/login'
            })
        },
        methodByPush: function (i) {
          this.array.push(i)
        },
    },
}
</script>

<style scoped>
.page {
    background-color: bisque;
}
</style>
