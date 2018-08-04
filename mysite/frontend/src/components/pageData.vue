<template>
    <ul>
        <board MID = '1' NUID='2'></board>
    </ul>
</template>

<script>
import board from './board'
export default {
    components: {
        board
    },
    name: 'pageData',
    created() {
        console.log('pageData')
    }
}
</script>

<style scoped>

</style>
