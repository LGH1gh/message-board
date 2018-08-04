<template>
    <div class='commit'>
        <ul class='comment-items'>
            <li v-for='comment in commentList'>
                <commentItem :username='comment.username' :comment='comment.comment' :time='comment.time'></commentItem>
            </li>
        </ul>
        <input type='text' contenteditable='true' placeholder='评论'>
    </div>
</template>

<script>
import commentItem from './commentItem'
export default {    
    name: 'comment',
    components: {
        commentItem
    },
    mounted: function() {
        this.get_comments(MID)
    },
    data() {
        commentList: []
    },
    props: {
        MID: {
            type: String,
            default: ''
        }
    },
    methods: {
        get_comments(MID) {
            this.$http.get('http://192.168.55.33:8000/api/get_comments', {params: {MID: MID}})
                .then((response) => {
                    let res = JSON.parse(response.bodyText)
                    console.log(res)
                    if (res.error_num == 0) {
                        this.commentList = res['list']
                    } else {
                        console.log(res['msg'])
                    }
                })
        }
    }
}
</script>

<style scoped>

</style>
