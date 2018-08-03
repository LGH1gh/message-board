<template>
    <div class='commentItem'>
        <a class='username'> {{ username}} </a> '&nbsp; : {{ comment }}'
        <div class='comment-detail'>{{ time }}</div>
    </div>
</template>

<script>
export default {
    name: 'commentItem',
    props: {
        username: {
            type: String,
            default: ''
        },
        comment: {
            type: String,
            default: ''
        },
        time: {
            type: String,
            default: ''
        }
    }
}
</script>

<style scoped>

</style>
