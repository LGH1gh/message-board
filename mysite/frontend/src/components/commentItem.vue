<template>
    <div class='commentItem'>
        <a class='username'> {{ username}} </a> '&nbsp; : {{ comment }}'
        <div class='comment-detail'>{{ time }}</div>
    </div>
</template>

<script>
export default {
    name: 'commentItem',
    data: function() {
        return {
            username: ''
        }
    },
    mounted: function() {
        this.get_username(this.UID)
    },
    props: {
        UID: {
            type:Number,
            default: 1
        },
        comment: {
            type: String,
            default: ''
        },
        time: {
            type: String,
            default: ''
        }
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
