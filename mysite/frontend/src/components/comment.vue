<template>
    <div class='comment'>
        <ul class='comment-items'>
            <li v-for='comment in commentList'>
                <commentItem :UID='comment.fields.UID' :comment='comment.fields.comment' :time='comment.fields.time'></commentItem>
            </li>
        </ul>
        <form @submit.prevent='add_comment'>
            <input type='text' contenteditable='true' placeholder='评论' v-model='userComment'>
            <input type='submit' value='提交'>
        </form>
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
        this.get_comments(this.MID)
    },
    data: function() {
        return {
            commentList: [],
            userComment: ''
        }
    },
    props: {
        MID: {
            type: String,
            default: ''
        },
        SUID: {
            type: Number,
            default: 0
        }
    },
    methods: {
        get_comments(MID) {
            this.$http.get('http://192.168.55.33:8000/api/get_comments', {params: {MID: MID}})
                .then((response) => {
                    let res = response.data
                    // console.log(res)
                    if (res.error_num == 0) {
                        this.commentList = res.list
                        // console.log(this.commentList)
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        add_comment() {
            this.$http.get('http://192.168.55.33:8000/api/add_comment', {params: {MID: this.MID, UID: this.SUID, comment: this.userComment}})
                .then((response) => {
                    let res = response.data
                    if (res.error_num == 0) {
                        this.get_comments(this.MID)
                        this.userComment = ''
                        // console.log(res.msg)
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
