<script>
	import { Icon } from '@steeze-ui/svelte-icon';
	import { ClipboardCopy } from '@steeze-ui/heroicons';

    let citationStyle;
    const citations = {
        'APA': `Reed, P.M., Hadjimichael, A., Malek, K., Karimi, T., Vernon, C.R., Srikrishnan, V., Gupta, R.S., Gold, D.F., Lee, B., Keller, K., Thurber, T.B., & Rice, J.S. (2022). Addressing Uncertainty in Multisector Dynamics Research [Book]. Zenodo. https://doi.org/10.5281/zenodo.6110623`,
        'BibTeX': `@book{Reed_Addressing_Uncertainty_2022,
    author = {Reed, Patrick M. and Hadjimichael, Antonia and Malek, Keyvan and Karimi, Tina and Vernon, Chris R. and Srikrishnan, Vivek and Gupta, Rohini S. and Gold, David F. and Lee, Ben and Keller, Klaus and Thurber, Travis B. and Rice, Jennie S.},
    doi = {10.5281/zenodo.6110623},
    publisher = {Zenodo},
    title = {{Addressing Uncertainty in Multisector Dynamics Research}},
    url = {https://uc-ebook.org},
    year = {2022}
}`,
    };

    const copyToClipboard = () => {
        try{
            navigator.clipboard.writeText(citations[citationStyle]);
        } catch(e) {
            // no op
        }
    };

</script>

<div class="flex flex-col items-center justify-center">
    <div class="mb-4">
        <select bind:value={citationStyle}>
            {#each Object.keys(citations) as citationStyle}
                <option value={citationStyle}>{citationStyle}</option>
            {/each}
        </select>
    </div>
    <div class="flex flex-row items-stretch justify-center">
        <div style="box-shadow: inset 0 2px 4px 0 rgb(0 0 0 / 0.2);" class="bg-slate-50 rounded-l-md overflow-auto">
            <pre
                class="m-4 text-sm text-slate-900 w-80 md:w-96 text-left leading-tight "
            >{citations[citationStyle] || ''}</pre>
        </div>
        <div on:click={copyToClipboard} title="Copy to clipboard" class="rounded-r-md drop-shadow p-2 bg-sky-700 hover:bg-sky-500 hover:cursor-pointer active:bg-orange-400">
            <Icon src={ClipboardCopy} class="icon w-6 text-slate-50" />
        </div>
    </div>
</div>