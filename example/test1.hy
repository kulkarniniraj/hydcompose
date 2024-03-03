(container
    :image "mariadb"
    :name "mariadb"
    :ports [(dict :host 13306 :container 3306)]
    :volumes [(dict :host "/home/niraj/Documents/tmp/mariadb" 
                   :container "/var/lib")]
    :env [(dict :key "MARIADB_ROOT_PASSWORD"
            :value "test123")])