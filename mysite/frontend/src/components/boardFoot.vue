<template>
    <div class='board-foot'>
        <div v-if='amAgree == 1' class='fa fa-thumbs-up'>
            {{ agreeNumber }}
        </div>
        <div v-else class='fa fa-thumbs-o-up'>
            {{ agreeNumber}}
        </div>
        <div v-if='amAgree == -1' class='fa fa-thumbs-down'>
            {{ disagreeNumber}}
        </div>
        <div v-else class='fa-thumbs-o-down'>

        </div>
    </div>
</template>

<script>
export default {
    name: 'boardFoot',
    props: {
        agreeNumber: {
            type: Number,
            default: 0
        },
        disagreeNumber: {
            type: Number,
            default: 0
        },
        amAgree: {
            type: Number,
            default: 0
        }
    },
    methods: {

    }
}
</script>

<style scoped>

</style>
