<template>
    <div class='board-head'>
        <div class='user-info' class='user'>
            <h3>用户名</h3>
            <div class='user-name'>
                {{ username }}
            </div>
            <h3>时间</h3>            
            <div class='user-detail'>
                {{ time }}
            </div>
        </div>
        <div class='board-info'>
            <h3>题目</h3>
            <div class='title'>
                {{ title }}
            </div>
            <h3>留言</h3>
            <div class='message'>
                {{ message }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'boardHead',
    data: function() {
        return {
            username: '',
        }
    },
    props: {
        UID: {
            type: Number,
            default: 0
        },
        time: {
            type: String,
            default: ''
        },
        title: {
            type: String,
            default: ''
        },
        message: {
            type: String,
            default: ''
        }
    },
    updated: function() {
        this.get_username(this.UID)
    },
    methods: {
        get_username(UID) {
            // console.log(UID)
            this.$http.get('http://localhost:8000/api/get_username', {params: {UID: UID}})
                .then((response) => {
                    let res = response.data
                    if (res.error_num == 0) {
                        this.username = res.username
                    } else {
                        console.log(res.msg)
                    }
                })
        }
    }
}
</script>

<style scoped>

</style>
