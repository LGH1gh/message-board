<template>
    <boardHead username='username' time='time' title='title' message='message'></boardHead>
    <boardFoot MID='MID' UID='UID'></boardFoot>
    <comment MID='MID'></comment>
</template>

<script>
import boardHead from './boardHead'
import boardFoot from './boardFoot'
import comment from './comment'
export default {
    name: 'board',
    props: {
        MID: {
            type: Number,
            default: 0
        }
    }
}
</script>

<style scoped>

</style>
