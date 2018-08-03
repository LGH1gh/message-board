<template>
import commentItemVue from './commentItem.vue';
    <ul class='comment'>
        <li v-for='(username, comment, time) in comments'>
            <commentItem :username='username' :comment='comment' :time='time'></commentItem>
        </li>
    </ul>
</template>

<script>
import commentItem from './commentItem'
export default {    
    name: 'comment',
    props: {
        UID: {
            type: String,
            default: ''
        },
        MID: {
            type: String,
            default: ''
        }
    }
}
</script>

<style scoped>

</style>
