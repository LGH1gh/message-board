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
            {{ disagreeNUmber }}
        </div>
    </div>
</template>

<script>
export default {
    name: 'boardFoot',
    props: {
        MID: {
            type: number,
            default: 0
        },
        UID: {
            type: number,
            default: 0
        }
    },
    methods: {

    }
}
</script>

<style scoped>

</style>
