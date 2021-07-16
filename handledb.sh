#!/bin/bash

dbname="bcoll"
username="gombb"
host="localhost"


add_new_product() {
    product_json=$(curl https://api.opensea.io/api/v1/asset/"$1"/"$2" )
    contract_address="$1"
    token_id="$2"
    img_url=$(echo $product_json | jq -r .image_url )
    name=$(echo $product_json | jq -r .name)
    description=$(echo $product_json | jq -r .description)
    base_price=$(echo $product_json  | jq -r .orders[-0].base_price)
    last_price=$(echo $product_json | jq -r .orders[-1].current_price)
    psql "$dbname" "$username" <<EOF
INSERT INTO "product"(contract_address, token_id, artist_id,
 base_price, last_price, img_url, description, name)
VALUES('$contract_address', '$token_id', '$3', '$base_price',
 '$last_price', '$img_url', '$description', '$name');
EOF
        
}


main() {
    if [[ "$1" == "add-product" ]]; then
        add_new_product "$2" "$3" "$4"
    elif [[ "$1" == "list-table" ]]; then
        list_table $2
    fi
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi


#add_product_args=[contract_address, token_id, artist_id]