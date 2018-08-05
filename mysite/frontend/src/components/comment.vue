<template>
    <div class='comment'>
        <h3>评论区</h3>
        <ul class='comment-items'>
            <li v-for='comment in commentList'>
                <commentItem :UID='comment.fields.UID' :comment='comment.fields.comment' :time='comment.fields.time'></commentItem>
            </li>
        </ul>
        
        <form @submit.prevent='add_comment'>
            <input type='text' contenteditable='true' placeholder='评论' v-model='userComment'>
            <input type='submit' value='提交'>
        </form>
        <div v-if='alert == 1' style='color: red'>请先登录，再评论</div>
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
            userComment: '',
            alert: 0
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
            if (this.SUID == 0) {
                this.alert = 1
            }
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
