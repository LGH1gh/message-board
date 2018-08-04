<template>
    <div class='commit'>
        <ul class='comment-items'>
            <li v-for='(username, comment, time) in comments'>
                <commentItem :username='username' :comment='comment' :time='time'></commentItem>
            </li>
        </ul>
        <input type='text' contenteditable='true' placeholder='评论'>
    </div>
</template>

<script>
import commentItem from './commentItem'
export default {    
    name: 'comment',
    props: {
        MID: {
            type: String,
            default: ''
        }
    },
    created: function (UID, MID) {

    }
}
</script>

<style scoped>

</style>
