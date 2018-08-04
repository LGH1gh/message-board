<template>
    <div class='board-head'>
        <div class='user-info'>
            <div class='user-name'>
                {{ username }}
            </div>
            <div class='user-detail'>
                {{ time }}
            </div>
        </div>
        <div class='board-info'>
            <div class='title'>
                {{ title }}
            </div>
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
            username: ''
        }
    },
    props: {
        UID: {
            type: String,
            default: ''
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
    mounted: function() {
        this.get_username(this.UID)
    },
    methods: {
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
        }
    }
}
</script>

<style scoped>

</style>
