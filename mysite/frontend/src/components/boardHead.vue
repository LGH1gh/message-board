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
    props: {
        username: {
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
    }
}
</script>

<style scoped>

</style>
